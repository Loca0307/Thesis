        ## Ask reviewers to edit their ACK the rebuttals
        venue = openreview.helpers.get_conference(client, request_form.id, setup=False)
        venue.custom_stage = openreview.stages.CustomStage(name='Rebuttal_Acknowledgement_Revision',
            child_invitations_name='Revision',
            reply_to='Rebuttal_Acknowledgement',
            reply_type=openreview.stages.CustomStage.ReplyType.REVISION,
            source=openreview.stages.CustomStage.Source.ALL_SUBMISSIONS,
            due_date=due_date,
            exp_date=due_date + datetime.timedelta(days=1),
            invitees=[openreview.stages.CustomStage.Participants.REPLYTO_REPLYTO_SIGNATURES],
            readers=[openreview.stages.CustomStage.Participants.REVIEWERS_SUBMITTED, openreview.stages.CustomStage.Participants.AUTHORS],
            content={
                'final_acknowledgement': {
                    'order': 1,
                    'description': "I acknowledge I read the rebuttal.",
                    'value': {
                        'param': {
                            'type': 'boolean',
                            'enum': [{ 'value': True, 'description': 'Yes, I acknowledge I read the rebuttal.' }],
                            'input': 'checkbox'
                        }
                    }
                }
            },
            notify_readers=True,
            email_sacs=False)

        venue.create_custom_stage()

        helpers.await_queue_edit(openreview_client, 'ICML.cc/2023/Conference/-/Rebuttal_Acknowledgement_Revision-0-1', count=1)

        ack_revision_invitations = openreview_client.get_invitations(invitation='ICML.cc/2023/Conference/-/Rebuttal_Acknowledgement_Revision')
        assert len(ack_revision_invitations) == 2

        ack_revision_invitation_ids = [invitation.id for invitation in ack_revision_invitations]
        assert 'ICML.cc/2023/Conference/Submission1/Rebuttal2/Rebuttal_Acknowledgement1/-/Revision' in ack_revision_invitation_ids
        assert 'ICML.cc/2023/Conference/Submission1/Rebuttal3/Rebuttal_Acknowledgement1/-/Revision' in ack_revision_invitation_ids

        revision_invitation = openreview_client.get_invitation('ICML.cc/2023/Conference/Submission1/Rebuttal2/Rebuttal_Acknowledgement1/-/Revision')
        assert revision_invitation.edit['note']['id'] == rebuttal_ack1_edit['note']['id']

        revision_invitation = openreview_client.get_invitation('ICML.cc/2023/Conference/Submission1/Rebuttal3/Rebuttal_Acknowledgement1/-/Revision')
        assert revision_invitation.edit['note']['id'] == rebuttal_ack2_edit['note']['id']
        
        rebuttal_ack2_revision_edit = reviewer_client.post_note_edit(
            invitation='ICML.cc/2023/Conference/Submission1/Rebuttal3/Rebuttal_Acknowledgement1/-/Revision',
            signatures=[anon_group_id],
            note=openreview.api.Note(
                content={
                    'final_acknowledgement': { 'value': True }
                }
            )
        )

        helpers.await_queue_edit(openreview_client, edit_id=rebuttal_ack2_revision_edit['id'])
