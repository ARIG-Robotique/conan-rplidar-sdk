from conans import ConanFile
from conans.tools import download, unzip, check_sha1
import os

class RPLidarSDKConan(ConanFile):
    name = "RPLidarSDK"
    version = "1.5.7"
    url = "https://github.com/ARIG-Robotique/conan-rplidar-sdk"
    description = "RPLidar SDK driver for Slamtech / RobotPeak lidar device"
    settings = "os", "compiler", "build_type", "arch"

    FOLDER_NAME = 'rplidar_sdk_v%s' % version

    def source(self):
        tarball_name = self.FOLDER_NAME + '.zip'
        download("http://www.slamtec.com/download/lidar/sdk/rplidar_sdk_v%s.zip" % self.version, tarball_name)
        check_sha1(tarball_name, "95452c5f32181b75ef151dbc62a3e2f59155de4c")
        unzip(tarball_name, self.FOLDER_NAME)
        os.unlink(tarball_name)

    def build(self):
        cmd = 'make -C %s/%s/sdk/sdk' % (self.conanfile_directory, self.FOLDER_NAME)
        self.output.info('Running Make: ' + cmd)
        self.run(cmd)

    def package(self):
        self.copy("*.h", dst="include", src="%s/sdk/sdk/include" % (self.FOLDER_NAME))
        if self.settings.os == "Windows":
            self.copy(pattern="*.lib", dst="lib", src="lib", keep_path=False)
        else:
            self.copy(pattern="*.a", dst="lib", src="%s/sdk/output/Linux/Release" % (self.FOLDER_NAME), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['rplidar_sdk']
