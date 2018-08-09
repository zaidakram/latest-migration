import sublime, sublime_plugin
import os
import re

class LatestMigrationCommand(sublime_plugin.WindowCommand):
  SUPPORTED_APPS = {
    'rails': {
      'folder':'db/migrate',
      'expected_items': [
        'Gemfile', 'app', 'config', 'db'
      ],
      'fe': 'rb', # File Extension
    },
    'amber': {
      'folder':'db/migrations',
      'expected_items': [
        'shard.yml', 'src', 'config', 'db'
      ],
      'fe': 'sql',
    }
  }

  def run(self):
    try:
      # Try to get a path from the currently open file.
      cur_path = self.window.active_view().file_name()
    except AttributeError:
      cur_path = None
      
    # If no file is open, try to get it from the currently open folders.
    if cur_path == None:
      if self.window.folders():
        cur_path = self.window.folders()[0]

    if cur_path:
      if os.path.isfile(cur_path):
        cur_path = os.path.dirname(cur_path)
      root, app_type = self.find_root(cur_path)
    else:
      raise NothingOpen("Please open a file or folder in order to search for the latest migration")

    if root:
      migrations_dir = os.path.join(root, LatestMigrationCommand.SUPPORTED_APPS[app_type]['folder'])
      migrations = os.listdir(migrations_dir)

      pattern = re.compile("^\d+_\w+.{0}$".format(LatestMigrationCommand.SUPPORTED_APPS[app_type]['fe']))
      migrations = sorted([m for m in migrations if pattern.match(m)])
      latest_migration = os.path.join(migrations_dir, migrations[-1])

      self.window.open_file(latest_migration)

  # Recursively searches each up a directory structure for the 
  # expected items that are common to a Rails/Amber application.
  def find_root(self, path):
    rails_expected_items = LatestMigrationCommand.SUPPORTED_APPS['rails']['expected_items']
    amber_expected_items = LatestMigrationCommand.SUPPORTED_APPS['amber']['expected_items']
    files = os.listdir(path)

    # The recursive search has gone too far and we've reached the system's
    # root directory! At this stage it's safe to assume that we won't come
    # across a familiar directory structure for supported app.
    if path == '/':
      raise NotSupportedApp("Cannot recognize this file structure as a Rails or Amber app")

    if len([x for x in rails_expected_items if x in files]) == len(rails_expected_items):
      return path, 'rails'
    elif len([x for x in amber_expected_items if x in files]) == len(amber_expected_items):
      return path, 'amber'
    else:
      return self.find_root(self.parent_path(path))

  # Returns the parent path of the path passed to it.
  def parent_path(self, path):
    return os.path.abspath(os.path.join(path, '..'))

class Error(Exception):
  def __init__(self, msg):
    self.msg = msg
    sublime.error_message(self.msg)

class NotSupportedApp(Error):
  pass
class NothingOpen(Error):
  pass
