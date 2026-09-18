#include <vector>
#include<iostream>
using namespace std;
class Solution {
    public:
     vector<int> twoSum(vector<int>&nums,int target) {
        int l,r;
        for(l=0;l<nums.size();l++){
            for(r=l+1;r<nums.size();r++){
                if(nums[l]+nums[r]==target){
                    return {l,r};
                }
            }
        }
        return {};
    }
}; 
int main(){
    vector<int> nums={2,7,11,15};
    int target=9;
Solution s;
vector<int> result=s.twoSum(nums,target);
cout<<result[0]<<" "<<result[1]<<endl;
return 0;
}