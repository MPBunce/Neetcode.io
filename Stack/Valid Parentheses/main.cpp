class Solution {
public:
    bool isValid(string s) {
        
        stack<char> st;
        
        for(auto i : s){
            if(i=='[' or i=='(' or i=='{'){
                st.push(i);
            }else{
                if(!st.empty()){
                    char ch = st.top();
                    if (i==']' and ch=='[' or i==')' and ch=='(' or i=='}' and ch=='{' ) {
                        st.pop();
                    }else{
                        return false;
                    }
                }else{
                    return false;
                }
            }
        }
        
        if(st.empty()) return true;
        return false;
    }
};