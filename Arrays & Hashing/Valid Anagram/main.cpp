class Solution {
public:
    bool isAnagram(string s, string t) {
        
        //so we have made two frequency arrays for checking the occurance of the alphabets in the string 
       int A[26] = {0}; 
       int B[26] = {0};
       
        //so s1 and s2 are the size of the strings respsectively 
        int s1 = s.size();
       int s2 = t.size();
        
        //here we have a flag to check conditions
       int flag =0;
        
        //if out strings have variable size then they cant be a anagram
       if(s1 != s2)
       {
           return false;
       }
        //a loop over string s
       for(int i=0; i<s1; i++)
       {
            //now mapping over the frequency array like map 
           A[s[i]-'a']++;
           B[t[i]-'a']++;
       }
        
        // now loop to check whether we have same number of elements or not
       for(int i=0; i<26; i++)
       {
           if(A[i]!=B[i])//if not
           {
               flag =1;//here we made flag =1 so that we can return false after the loop 
               break;
           }
       }
       if(flag==1)//her we have returned false 
       return false;
       else
           //else its a anagram
       return true;
        
    }
};

// Shorter

class Solution {
public:
    
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        
        int n = s.length();
        unordered_map<char, int> counts;
        for (int i = 0; i < n; i++) {
            counts[s[i]]++;
            counts[t[i]]--;
        }
        for (auto count : counts){
            if (count.second){
                return false;   
            }         
        }

        return true;
        
    }
};

// Sorting

class Solution {
public:
    bool isAnagram(string s, string t) {       
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        if(s.size() != t.size()){return false;}
        
        for(int i = 0; i < s.size(); i++){
            if(s[i] != t[i]){return false;}
        }
        
        return true;
    }
};

//sorting with less code

class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        
        return s==t;
    }
};