import pandas as pd


class Processor:

    def build_log_stats(self, log_window):
        df = pd.DataFrame(log_window,
                          columns=["remotehost", "rfc931", "authuser", "date", "request", "status", "bytes"])
        status_info = df['request'].groupby(df['status']).value_counts().to_string()
        top_request = df.groupby('request')['request'].count().sort_values(ascending=False).head(1).to_string()
        return {"Top Requests Section": top_request, "Debug Stats": status_info}
