import pandas as pd

class proccesor():

    def build_log_stats(log_window):
        df = pd.DataFrame(log_window,
                          columns=["remotehost", "rfc931", "authuser", "date", "request", "status", "bytes"])
        return df['request'].groupby(df['status']).value_counts().to_string()
    # distro =df.groupby('request')['request'].count()
        # print("Request Distribution")
        # print(distro)
        # print("------------------------------------")
        # print(df.groupby('status')['status'].count())
        # print(self.current_window)