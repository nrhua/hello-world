from conans import ConanFile, CMake, tools


class ExampleConan(ConanFile):
    name = "hello-jenkins"
    version = '1.0.0'
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Example here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src*", "CMakeLists.txt", "test*"
    short_paths = True
    build_policy = 'missing'

    def requirements(self):
        if self.develop:
            self.requires('gtest/1.8.0@bincrafters/stable')

    def imports(self):
        self.copy(pattern='*.dll', dst='bin', src='bin')
        self.copy(pattern='*.a', dst='lib', src='lib')
        self.copy(pattern='*.so*', dst='lib', src='lib')
        self.copy(pattern='*.dylib*', dst='bin', src='lib')

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]


