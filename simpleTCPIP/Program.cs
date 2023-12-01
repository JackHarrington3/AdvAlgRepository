using System.Net.Http;
using System.Threading.Tasks;
using System;

namespace simpleTCPIP {

    class Program {

        public static void Main(String[] args) {
            
            Task<string> result = getWord("adjective");
            Console.WriteLine(result.Result);
        }

        public static async Task<string> getWord(string wordType) {
            HttpClient client  = new HttpClient();
            string html = await client.GetStringAsync(@"https://www.randomword.com/" + wordType);
            int startIndex = html.IndexOf("<div id=\"random_word\"");
            html = html.Substring(startIndex+22);
            int endIndex = html.IndexOf("</div>");
            var theWord = html.Substring(0,endIndex);
            return theWord;
        }

    }

}