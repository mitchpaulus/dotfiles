function vtag --description 'Create git tag used for versioning'
    check_version $argv[1]
    and git tag $argv[1]
    and git push --tags origin $argv[1]
end
