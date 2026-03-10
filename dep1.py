import pandas as pd

class DataTransformer:
    """
    Transforms raw event data into aggregated statistics.
    """

    def _to_dataframe(self, data):
        """Converts list of records to pandas DataFrame."""
        df = pd.DataFrame(data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df

    def get_session_stats(self, data, source_name=""):
        """Calculates session duration statistics per user."""
        df = self._to_dataframe(data)
        stats = df.groupby('user_id')['duration_ms'].agg(['sum', 'mean', 'count']).reset_index()
        stats.columns = ['user_id', f'{source_name}_duration_sum', f'{source_name}_duration_mean', f'{source_name}_session_count']
        return stats

    def get_page_views(self, data, source_name=""):
        """Counts page views per page."""
        df = self._to_dataframe(data)
        page_views = df[df['event'] == 'page_view']['page'].value_counts().reset_index()
        page_views.columns = ['page', f'{source_name}_view_count']
        return page_views
