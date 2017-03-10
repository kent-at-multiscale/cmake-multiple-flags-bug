import os

import conans


class CMakeMultipleFlagsBugTest(conans.ConanFile):
    """
    A reproduction test case for the cmake multiple flags bug.
    """
    settings = 'os', 'compiler', 'build_type', 'arch'
    exports_sources = 'CMakeLists.txt', 'main.cpp'
    requires = 'cmake-multiple-flags-bug/1.0.0@kent_at_multiscale/stable'
    generators = 'cmake', 'env', 'txt'
    
    def system_requirements(self):
        if self.scope.installTools:
            try:
                installer = conans.tools.SystemPackageTool()
                installer.update()
                installer.install('cmake')
            except:
                self.output.warn('Unable to bootstrap required build tools.  If they are already installed, you can ignore this warning.')
    
    def build(self):
        cmake = conans.CMake(self.settings)
        
        args = []
        vars = {}
        if self.scope.verbose:
            vars['CMAKE_VERBOSE_MAKEFILE'] = 'ON'
        else:
            vars['CMAKE_VERBOSE_MAKEFILE'] = 'OFF'
        
        cpu_count = conans.tools.cpu_count()
        self.output.info('Detected %s CPUs' % (cpu_count))
        
        self.output.info('Creating build scripts')
        cmake.configure(self, args, vars)
        
        self.output.info('Compiling')
        cmake.build(self, ['--', '-j%s' % (cpu_count)])
        
        self.output.info('Running tests')
        self.run('ctest --parallel %s' % (cpu_count))
    
    def test(self):
        cpu_count = conans.tools.cpu_count()
        self.output.info('Detected %s CPUs' % cpu_count)
        
        self.output.info('Running tests')
        self.run('ctest --parallel %s' % (cpu_count))
