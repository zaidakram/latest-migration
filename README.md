# Latest Migration

Opens the latest migration created in a supported web frameworks. Works with Sublime Text 3 and Sublime Text 2.

### Supported Web Frameworks

  * Ruby on Rails
  * Amber

## Usage

* Through Command Pallette 

1. Open any file in your app.
2. Bring up your command pallette (`Cmd + Shift + P` / `Ctrl + Shift + P`) and type in:
  ```
  latest
  ```
3. In no time the "Latest Migration: Open latest migration" should be highlighted
4. Hit enter, and lo and behold; your latest migration!

* Through Key Bindings

1. Click on `Preferences > Key Bindings`
2. In the right section you can assign any keyboard shortcut of your liking to the command, for example:
```
  { "keys": ["ctrl+shift+0"], "command": "latest_migration"}
```
3. Make sure your key combination don't collide with any other command shortcut.
4. That is it!

## TODOs

- [x] Amber
- [ ] Phoenix
- [ ] Any other ?

## Special Thanks

To [Alex Plescan](https://github.com/alexpls) for Providing the original [Rails Latest Migration](https://github.com/alexpls/Rails-Latest-Migration) plugin, which inspired this one.


## License
The MIT License (MIT) - for more info see [LICENSE.md](https://github.com/zaidakram/latest-migration/blob/master/LICENSE.md).
