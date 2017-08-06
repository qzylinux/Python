clear all;
%读入融合后的数据
fused_data=load('fused_data.txt');
%存储标号
label=fused_data(:,1);
%存储数据
data1=fused_data(:,2);
data=round(data1/10)*10
figure(1);
plot(label,data);
hold on;

%N表示有多少个片段参与判断,n表示每个片段有多少数据
N=60;
n=20;
%阈值
Pth=0.70;
%用来记录目前是在检测第几个片段
Loc=1;
%存储用来做对比的正常数据，长度为n*(N-1)
Normal_Data=data( 1:(n*(N-1)) );
%用来存储进行检测的数据段，长度为n*N
Detect_Data=zeros(1,n*N);
% %f_work表示是否继续进行泄漏检测
% f_work=1;
%Acf存储每个片段的自相关函数
Acf=zeros(N,n);
%L_acf存储各个片段彼此间的距离
Len_Acf=zeros(N,N);
%用来存储Len_Acf每一列的平均值
Len_Acf_Mean=zeros(1,N);
%用来存放所有的待检测序列的权重，即所有Len_Acf_Mean的最后一后一个值
Len_Acf_Mean_all=zeros(1,1000);
%将正常数据Normal_Data 转置 之后赋值给Detect_Data前n*(N-1)
Detect_Data=Normal_Data';
%存储异常片段的位置
Res_Loc=[];
Num=1;

%由于片段相关性矩阵只有最后一列和最后一行在变，前面的是固定的，所以写在循环外面
%.....................第一步求自相关函数.........................%    
    %检测算法，第一步计算检测序列中每个片段的自相关函数，共N个片段
for i=1:N-1
    %取出一个片段
    x=Detect_Data(1+(i-1)*n : n*i);
    %求取出片段的自相关函数
     %防止方差为0，自相关函数无意义
    if var(x)==0
        x(2)=x(2)+0.001
    end
    [ACF,lags,bounds]=autocorr(x,n-1);
    %将求得的自相关函数赋值给Acf存储
    for j=1:n
        Acf(i,j)=ACF(j);
    end   
end
%.....................第二步求片段间的相关性.....................%
for i=1:N-2
    for j=i+1:N-1
        %先求向量点乘，然后除以两个向量的模的乘积
        c=dot( Acf(i,:),Acf(j,:) )/( norm(Acf(i,:)) * norm(Acf(j,:)) );
%         C=(Acf(i,:)-Acf(j,:)).^2;
%         c=sqrt(sum(C(:))); 
        Len_Acf(i,j)=c;
        Len_Acf(j,i)=Len_Acf(i,j)
    end
end
% %将阈值设置为前N-1个片段相关性的最小值
% Len_Acf_Mean=mean(Len_Acf);
% Pth=min(Len_Acf_Mean(1:N-1));

%..........................................................................
%............................循环分割线....................................。
%..........................................................................
%融合的数据达到一个片段的个数就进行一次判定
while Loc<=(9990/n-1)
    %将目前检测的片段加入到检测序列，长度为n
    for i=1:n
       Detect_Data(n*(N-1)+i)=data(n*(Loc-1)+i);
    end
   
%.....................第一步求自相关函数.........................%    
%检测算法，第一步计算检测序列中每个片段的自相关函数，共N个片段，循环外计算了N-1个片段
    %取出第N个片段
    x=Detect_Data(1+(N-1)*n : n*N);
    %防止方差为0，自相关函数无意义
    if var(x)==0
        x(1)=x(1)+0.001
    end
    %求取出片段的自相关函数
    [ACF,lags,bounds]=autocorr(x,n-1);
    %将求得的自相关函数赋值给Acf存储
    for j=1:n
        Acf(N,j)=ACF(j);
    end   
%.....................第二步求片段间的相关性.....................%
    for i=1:N-1
        %先求向量点乘，然后除以两个向量的模的乘积
        c=dot( Acf(i,:),Acf(N,:) )/( norm(Acf(i,:)) * norm(Acf(N,:)) );
%         C=(Acf(i,:)-Acf(N,:)).^2;
%         c=sqrt(sum(C(:))); 
        Len_Acf(i,N)=c;
        Len_Acf(N,i)=Len_Acf(i,N)
    end
%.....................第三步找出异常部分，做出判断...............%    
    %求Len_Acf每一列的平均值
    Len_Acf_Mean=mean(Len_Acf)*N/(N-1);
    %把最后一列的平均值保存起来
    Len_Acf_Mean_all(Loc)=Len_Acf_Mean(N);
    %判断待检测片段是否正常
    figure(1);
    if Len_Acf_Mean(N)<Pth
        MMM=mean(Detect_Data(n*(N-1)+1:n*N));
        %if MMM>50
            plot(Loc*n-n/2,1:200,'-r');
            hold on;
             %记录下那个片段有异常
            Res_Loc(Num)=Loc;
            Num=Num+1;
       % end
    end
    %更新Loc
    Loc=Loc+1;
%     %更新f_work
%     f_work=f_work+1;
end