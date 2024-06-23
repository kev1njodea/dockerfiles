# containrrr / watchtower

- https://github.com/containrrr/watchtower
- https://containrrr.dev/watchtower/

## Notes

I only run this manually at the moment.

## Arguments

- https://containrrr.dev/watchtower/arguments/

```
command: --run-once --cleanup --label-enable
```

- `--run-once`

> Run an update attempt against a container name list one time immediately and exit.

- `--cleanup`

> Removes old images after updating. When this flag is specified, watchtower will remove the old image after restarting a container with a new image. Use this option to prevent the accumulation of orphaned images on your system as containers are updated.

- `--label-enable`

> Monitor and update containers that have a com.centurylinklabs.watchtower.enable label set to true.
