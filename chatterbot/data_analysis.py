import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DataProcessor:
    def __init__(self):

        self.keywords_df = pd.read_csv('keywords.csv')
        self.items_df = pd.read_csv('items.csv')


    def get_top_keywords(self):
        """
        Returns the top N keywords based on the 'order' column.
        """
        top_5_keywords = self.keywords_df.nlargest(5, 'order')
        top_5_keywords = top_5_keywords[['keyword', 'order']].sort_values(by='order', ascending=False)
        keywords = " " 
        for i in top_5_keywords['keyword']:
            if i != 'keyword' or i is not int:
                keywords += i + ", "
        return keywords

    
    def get_match_items(self):
        
        # Normalize item names for basic match
        self.keywords_df['keyword_lower'] = self.keywords_df['keyword'].str.lower()
        self.items_df['item_name_lower'] = self.items_df['item_name'].str.lower()

        # Inner merge (exact string match on lower-case names)
        self.merged_df = pd.merge(self.keywords_df, self.items_df, left_on='keyword_lower', right_on='item_name_lower', how='inner')
        matched = " "
        for i in self.merged_df['keyword']:
            if i != 'keyword' or i is not int:
                matched += i + ", "
        return matched
        #return (f"\nMatched items: {len(self.merged_df)}\n{self.merged_df[['keyword', 'item_name', 'order', 'item_price', 'cuisine_tag']].head()}")
    
    def cuisine_stats(self):
        self.keywords_df['keyword_lower'] = self.keywords_df['keyword'].str.lower()
        self.items_df['item_name_lower'] = self.items_df['item_name'].str.lower()

        # Inner merge (exact string match on lower-case names)
        self.merged_df = pd.merge(self.keywords_df, self.items_df, left_on='keyword_lower', right_on='item_name_lower', how='inner')
        
        
        
        cuisine_stats = self.merged_df.groupby('cuisine_tag')[['view', 'menu', 'checkout', 'order']].sum().sort_values(by='order', ascending=False)
        return (f"nCuisine Performance:\n{cuisine_stats}")

    def plot_data(self):
        self.keywords_df['keyword_lower'] = self.keywords_df['keyword'].str.lower()
        self.items_df['item_name_lower'] = self.items_df['item_name'].str.lower()

        # Inner merge (exact string match on lower-case names)
        self.merged_df = pd.merge(self.keywords_df, self.items_df, left_on='keyword_lower', right_on='item_name_lower', how='inner')
        
        
        plt.figure(figsize=(10,6))
        sns.scatterplot(data=self.merged_df, x='item_price', y='order', hue='cuisine_tag', palette='tab10')
        plt.title('Price vs Order Count by Cuisine')
        plt.xlabel('Item Price')
        plt.ylabel('Order Count')
        plt.legend(title='Cuisine', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.subplots_adjust(right=0.75)
        plt.tight_layout()

        self.merged_df.to_csv('merged_keyword_item_data.csv', index=False)
        
        path = "static/scatter_plot.png"
        plt.savefig(path)
        plt.close()
        
        return path