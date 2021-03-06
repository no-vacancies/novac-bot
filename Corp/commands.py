from Corp.config import SRP_USAGE
from Corp.controller import submit_srp, valid_lossmail, valid_character


class CorpBot:
    def __init__(self, bot):

        @bot.command('srp', help='Submit for SRP from within discord. {}'.format(SRP_USAGE))
        async def srp(channel, arg, user):
            try:
                args = arg.split(",", 2)
                url = args[1].strip().replace('<', '').replace('>', '')
                loss_valid = valid_lossmail(url)
                character_valid = valid_character(args[0])
                submitted_by = 'Submitted by ' + str(user)
                if loss_valid and character_valid:
                    if len(args) == 3:
                        submit_srp(args[0], url, submitted_by, args[2])
                    else:
                        submit_srp(args[0], url, submitted_by)
                    message = "SRP submitted."
                elif not loss_valid:
                    message = 'Invalid lossmail, please try again.'.format(SRP_USAGE)
                else: # character not valid
                    message = 'Invalid character, please try again.'.format(SRP_USAGE)
            except (AttributeError, IndexError) as e:  # If user doesn't enter 2 or 3 arguments (CSV's)
                print(e)
                message = 'Invalid arguments. {}'.format(SRP_USAGE)

            return await bot.post_message(channel, message)
