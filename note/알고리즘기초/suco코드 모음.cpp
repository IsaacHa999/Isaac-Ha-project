// // // // Sum-of-Subsets Problem
// // // void sum_of_subsets (index i, int weight, int total) {
// // //     if (promising(i)) {
// // //         if (weight == W ) 
// // //             cout << include [1] through include[i];
// // //         else {
// // //             include[i+1] = "yes";
// // //             sum_of_subsets(i+1, weithg + w[ii+1], total - w[i+1]);
// // //             include[i+1] = "no";
// // //             sum_of_subsets(i+1, weight, total-w[i+1]);
// // //         }
// // //     }
// // // }

// // // bool promising (index i) {
// // //     return (weight + total = W)
// // //      && (weight == W || weight + w[i+1] <= W);
// // // }

// // // Graph Coloring
// // void m_coloring (index i) {
// //     int color;
// //     if (promising(i)) 
// //         if (i == n) cout <<vcolor[1] through vcolor[n];
// //         else 
// //             for (color = 1; color <= m; color++) {
// //                 vcolor[i+1] = color;
// //                 m_coloring(i+1);
// //             }
// // }

// // bool promising (index i ) {
// //     int j; 
// //     bool switch1;
// //     switch1 = TRUE;
// //     j = 2;
// //     while (j <i && switch1) {
// //         if (W[i][j] && vcolor[i] == vcolor[j]) switch1 = FALSE;
// //         j++;
// //     }
// //     return switch1;
// // }

// // #define index int
// void knapsack (index i, int profit, int weight) {
//     if (weight <= W && profit > maxprofit) {
//         maxprofit = profit;
//         numbest = i;
//         bestset = include;
//     }

//     if (promising(i)) {
//         include[i+1] = "YES";
//         knapsack(i+1,profit + p[i+1], weight + w[i+1]);
//         include[i+1] = "NO";
//         knapsack(i+1, profit, weight);
//     }
// }

// bool promising(index i) {
//     index j, k;
//     int totweight;
//     float bound;
//     if (weight >= W) return false;
//     else {
//         j = i+1;
//         bound = profit;
//         totweight = weight;
//         while ((j <= n) && (totweight + w[j] <= W)) {
//             totweight = totweight + w[j];
//             bound = bound + p[j];
//             j++;
//         }
//         k = j;
//         if (k <= n)
//             bound = bound + (W-totweight) *(p[k]/w[k]);
//         return bound > maxprofit
//     }
// }