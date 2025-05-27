          .update(schema.monitor)
          .set({ status: "active" })
          .where(eq(schema.monitor.id, monitor.id));

        // we can't have a monitor in error without an incident
        if (monitor.status === "error") {
          const incident = await db
            .select()
            .from(incidentTable)
            .where(
              and(
                eq(incidentTable.monitorId, Number(monitorId)),
                isNull(incidentTable.resolvedAt),
                isNull(incidentTable.acknowledgedAt),
              ),
            )
            .get();

          if (!incident) {
            // it was just a single failure not a proper incident
            break;
          }
          if (incident?.resolvedAt) {
            // incident is already resolved
            break;
          }

          console.log(`🤓 recovering incident ${incident.id}`);
          await db
            .update(incidentTable)
            .set({
              resolvedAt: new Date(cronTimestamp),
              autoResolved: true,
            })
            .where(eq(incidentTable.id, incident.id))
            .run();
        }