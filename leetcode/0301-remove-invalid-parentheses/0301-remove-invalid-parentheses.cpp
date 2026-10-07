class Solution {
public:
    bool valid(string& s) {
        int cnt = 0;

        for(char c: s){
            if(c == '('){
                cnt++;
            }
            else if(c == ')'){
                cnt--;

                if(cnt < 0){
                    return false;
                }
            }
        }

        return cnt == 0;
    }

    vector<string> removeInvalidParentheses(string s) {
        vector<int> pos;

        for(int i = 0; i < s.size(); i++){
            if(s[i] == '(' || s[i] == ')'){
                pos.push_back(i);
            }
        }

        int p = pos.size();
        int minRemove = p;
        unordered_set<string> st;

        for(int mask = 0; mask < (1 << p); mask++){
            int removed = __builtin_popcount(mask);

            if(removed > minRemove){
                continue;
            }

            string temp;
            int j = 0;

            for(int i = 0; i < s.size(); i++){
                if(j < p && pos[j] == i){
                    if(mask & (1 << j)){
                        j++;
                        continue;
                    }

                    j++;
                }

                temp += s[i];
            }

            if(valid(temp)){
                if(removed < minRemove){
                    minRemove = removed;
                    st.clear();
                }

                st.insert(temp);
            }
        }

        return vector<string>(st.begin(), st.end());
    }
};