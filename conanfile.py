from conans import ConanFile, tools


class SparkleConan(ConanFile):
    name = "sparkle"
    version = "1.21.3"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Sparkle here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    no_copy_source = True

    def source(self):
        url = "https://github.com/sparkle-project/Sparkle/releases/download/{version}/Sparkle-{version}.tar.bz2".format(version=self.version)
        tools.get(url)

    def package(self):
        self.copy("*", symlinks=True)

    def package_info(self):
        f_location = '-F "%s"' % self.package_folder
        self.cpp_info.cxxflags.append(f_location)
        self.cpp_info.sharedlinkflags.extend([f_location, "-framework Sparkle"])
        self.cpp_info.exelinkflags = self.cpp_info.sharedlinkflags

