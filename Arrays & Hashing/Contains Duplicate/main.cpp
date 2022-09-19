//Time Limit Exceeded 
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        vector<int> set;
           
        for(int i = 0; i < nums.size(); ++i){
            
            if (std::find(set.begin(), set.end(), nums[i]) != set.end()) {
                return true;
            }
            
            set.push_back(nums[i]);
            
        }
            
        return false;
        
    }
};

//Accepted

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        bool Flag = false;
        unordered_map<int, int> table;
        
        for(int i = 0; i < nums.size(); ++i){
            
            table[nums[i]]++;
            
            if(table[nums[i]] > 1){
                Flag = true;
                break;
            }
            
        }
        
        
        return Flag;
        
    }
};