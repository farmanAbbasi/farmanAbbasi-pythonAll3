    df=[[-1 for x in range(m+1)] for y in range(n+1)]
    print(df)
    
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                df[i][j]=0
            elif Y[i-1]==X[j-1]:
                df[i][j]=df[i-1][j-1]+1
            else:
                df[i][j]=max(df[i][j-1],df[i-1][j])
    print(df)
    return df[n][m]   
