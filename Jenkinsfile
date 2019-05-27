@Library('jenny@nrh/test_version') _

jennyPipeline{
    nodeConfigs = [
        [
            nodeName: 'Linux',
            awsAmi: 'redhat-gcc8-beta',
            conanProfiles: ['gcc-8.2-release', 'gcc-8.2-debug'],
            primaryNode: true,
        ],  
        [
            nodeName: 'Windows',
            label: 'win && current',
            conanProfiles: ['vs-15-release', 'vs-15-debug'],
            primaryNode: true,
        ],
        [
            nodeName: 'Apple',
            label: 'mac && current',
            conanProfiles: ['apple-clang-10.0-release', 'apple-clang-10.0-debug'],
        ],  
    ]
    projectConfig = [
        projectName: 'jenny-canary',
        conanDependencyRepos: ['conan-local'],
        conanUploadRepo: 'conan-local',
        npmUploadRepo: 'npm-local-ksf',
        pythonUploadRepo: 'pypi-local-ksf',
        sendSlackNotifications: '#kosi-test',
        shouldPublish: true,
        updateKosiHub: true,
        runSonarQube: false,
        runBlackDuck: false
    ]
    packageConfigs = [
        [
            conan: true,
            dir: 'helloworld',
            packageName: 'hello-jenkins', 
            testPackageDirectory: 'test/package',
            conanChannel: 'keysight/stable',
        ],        
     ]
}
