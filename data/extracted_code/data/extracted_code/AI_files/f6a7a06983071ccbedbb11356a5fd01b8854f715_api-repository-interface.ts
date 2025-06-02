
  async getMatchLogs(matchId: String): Promise<MatchStateDto> {
    const url = urlcat('/game/admin/:matchId/logs', {
      matchId,
    });
    let result;
    try {
      result = await ApiAxios.instance().get(url);
    } catch (e: any) {
      const err = makeAxiosError(e);
      console.error(err.message)
      // here we can set message according to status (or data)
      throw new Error('Váratlan hiba történt');
    }
    return result.data;
  }