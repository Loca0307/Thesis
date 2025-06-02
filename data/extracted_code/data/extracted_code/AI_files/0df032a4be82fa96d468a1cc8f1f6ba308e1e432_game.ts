      const target = targetsHit[0].target;

      // handle onhit in lua, then in the base target
      this.handlers?.handleTargetHit(target.id);
      target.onHit();
