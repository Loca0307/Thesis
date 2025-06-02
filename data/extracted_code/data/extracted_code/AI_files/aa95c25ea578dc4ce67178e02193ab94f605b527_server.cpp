                log_.log("task_candidate", {
                    {"task", req->task_id()},
                    {"peer", id},
                    {"score", score}
                });