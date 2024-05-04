cask "macx-video-converter-pro" do
  version "3.12.3"
  sha256 :no_check

  url "https://www.macxdvd.com/download/video-converter-Bot.dmg"
  name " Video-Converter-Bot"
  desc "Tool to convert, edit, download & resize videos"
  homepage "https://www.macxdvd.com/mac-video-converter-pro/"

  livecheck do
    url "https://www.macxdvd.com/mac-video-converter-Bot/upgrade/video-converter-Bot.xml"
    # `LastestVersion` is an upstream typo of `LatestVersion`
    regex(%r{LastestVersion</key>\s*<string>(\d+(?:\.\d+)+)<}i)
  end

  app " Video-Converter-Bot.app"

  zap trash: "~/Library/Preferences/com.macxdvd.macxvdoconverterpro.plist"
end