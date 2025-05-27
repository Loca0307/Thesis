        const RepoPlugin = Settings.PLUGINS.repository
        return new RepoPlugin(this.nop, this.github, repo, repoConfig, this.installation_id, this.log, this.errors).sync().then(res => {
          this.appendToResults(res)
          return Promise.all(
            childPlugins.map(([Plugin, config]) => {
              return new Plugin(this.nop, this.github, repo, config, this.log, this.errors).sync()
            }))
        }).then(res => {
          this.appendToResults(res)
        })
      } catch (e) {
        if (this.nop) {
          const nopcommand = new NopCommand(this.constructor.name, this.repo, null, `${e}`, 'ERROR')
          this.log.error(`NOPCOMMAND ${JSON.stringify(nopcommand)}`)
          this.appendToResults([nopcommand])
          // throw e
        } else {
          throw e
        }