`9A19103F-16F7-4668-BE54-9A1E7A4F7556`

In `sln` files that is the new ASP.NET core project type GUID.

`FAE04EC0-301F-11D3-BF4B-00C04F79EFBC` was the old one.


## MAUI

- [Tutorials](https://learn.microsoft.com/en-us/training/paths/build-apps-with-dotnet-maui/?WT.mc_id=dotnet-35129-website)


## Avalonia

<https://avaloniaui.net/>

## Ubuntu

When trying to get the dotnet tool `svcutil` to work, I kept running into errors saying the framework wasn't found.

I think that it had to do something with Ubuntu's version of the package.
I followed the steps at <https://askubuntu.com/a/1423089/1653412> which involved:

```
sudo apt remove 'dotnet*'
sudo apt remove 'aspnetcore*'
sudo touch /etc/apt/preferences.d/dotnet.pref

# Content
# Package: *
# Pin: origin "packages.microsoft.com"
# Pin-Priority: 1001
printf "Package: *\nPin: origin \"packages.microsoft.com\"\nPin-Priority: 1001\n" | sudo tee /etc/apt/preferences.d/dotnet.pref

# Do PPA installation stuff below.

sudo apt update
sudo apt install dotnet-sdk-6.0
```

Similar steps described here:
<https://learn.microsoft.com/en-us/dotnet/core/install/linux-package-mixup?pivots=os-linux-ubuntu#i-need-a-version-of-net-that-isnt-provided-by-my-linux-distribution>


## Installation

```
# XXXXX should be 22.04 etc.
# Download Microsoft signing key and repository
wget https://packages.microsoft.com/config/ubuntu/XXXXXXXXXXXXX/packages-microsoft-prod.deb -O packages-microsoft-prod.deb

# Install Microsoft signing key and repository
sudo dpkg -i packages-microsoft-prod.deb

# Clean up
rm packages-microsoft-prod.deb

# Update packages
sudo apt update
```
