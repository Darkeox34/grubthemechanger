# GRUB Theme Manager

A simple Python script to manage and apply GRUB themes on Linux systems. This tool allows you to easily switch between installed GRUB themes with an interactive command-line interface.

## Features

- 🎨 Interactive theme selection menu
- 🔒 Automatic backup of GRUB configuration
- ✅ Safe theme application with error handling
- 🛡️ Superuser privilege checking
- 📁 Automatic GRUB configuration regeneration

## Requirements

- Linux system with GRUB bootloader
- Python 3.x
- Superuser (root) privileges
- GRUB themes installed in `/boot/grub/themes/`

## Installation

1. Clone this repository or download the script:
```bash
git clone <your-repository-url>
cd grub-theme-manager
```

2. Make the script executable:
```bash
chmod +x grub_theme_manager.py
```

## Usage

Run the script with superuser privileges:

```bash
sudo python3 grub_theme_manager.py
```

The script will:
1. Check for superuser privileges
2. Display all available themes in `/boot/grub/themes/`
3. Allow you to select a theme interactively
4. Create a backup of your current GRUB configuration
5. Apply the selected theme
6. Regenerate the GRUB configuration

### Example Output

```
Available themes: 
(1) breeze
(2) ubuntu-mate
(3) stylish
Please select the theme you want to use: 
2
You have selected the theme ubuntu-mate, do you want to apply this theme? (y/n)
y
Creating a backup copy of grub config!
Backup directory created at /path/to/script/backup
Backup of grub config created at /path/to/script/backup/grub
Theme ubuntu-mate applied successfully!
grub-mkconfig executed successfully!
```

## How It Works

### Directory Structure

The script expects GRUB themes to be installed in the following structure:
```
/boot/grub/themes/
├── theme1/
│   └── theme.txt
├── theme2/
│   └── theme.txt
└── theme3/
    └── theme.txt
```

### Backup System

Before making any changes, the script automatically creates a backup of your GRUB configuration:
- Backup location: `./backup/grub` (relative to script location)
- The backup directory is created automatically if it doesn't exist

### Configuration Process

1. **Backup**: Creates a safety backup of `/etc/default/grub`
2. **Modify**: Updates the `GRUB_THEME` line in the configuration
3. **Apply**: Runs `grub-mkconfig` to regenerate the GRUB configuration file

## Safety Features

- **Privilege Check**: Ensures the script is run with sudo
- **File Validation**: Verifies theme files exist before applying
- **Backup Creation**: Automatically backs up configuration before changes
- **Error Handling**: Comprehensive error checking and user feedback
- **Input Validation**: Validates user input for theme selection

## Troubleshooting

### Common Issues

**"This script requires superuser privileges"**
- Solution: Run the script with `sudo`

**"Path /boot/grub/themes/ doesn't exist"**
- Solution: Install GRUB themes first, or check if GRUB is properly installed

**"theme.txt does not exist"**
- Solution: Ensure the selected theme has a proper `theme.txt` file

**"Error executing grub-mkconfig"**
- Solution: Check if GRUB is properly configured and you have write permissions

### Restoring from Backup

If something goes wrong, you can restore your original GRUB configuration:

```bash
sudo cp ./backup/grub /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

## Installing GRUB Themes

To install new GRUB themes:

1. Download a GRUB theme
2. Extract it to `/boot/grub/themes/`
3. Ensure it contains a `theme.txt` file
4. Run this script to apply it

Example:
```bash
sudo mkdir -p /boot/grub/themes/mytheme
sudo cp -r downloaded-theme/* /boot/grub/themes/mytheme/
sudo python3 grub_theme_manager.py
```

## Supported Systems

This script has been tested on:
- Ubuntu and derivatives
- Debian
- Fedora
- Arch Linux
- Most Linux distributions using GRUB2

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is released under the MIT License. See LICENSE file for details.

## Disclaimer

This script modifies system bootloader configuration. While it includes safety features and backup mechanisms, use it at your own risk. Always ensure you have a way to recover your system (live USB, etc.) before making bootloader changes.

## Support

If you encounter issues:
1. Check the troubleshooting section
2. Ensure you have proper backups
3. Open an issue on GitHub with error details and system information

---

**Note**: Always test GRUB themes in a safe environment before applying them to production systems.
