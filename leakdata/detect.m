clear all;
%�����ںϺ������
fused_data=load('fused_data.txt');
%�洢���
label=fused_data(:,1);
%�洢����
data1=fused_data(:,2);
data=round(data1/10)*10
figure(1);
plot(label,data);
hold on;

%N��ʾ�ж��ٸ�Ƭ�β����ж�,n��ʾÿ��Ƭ���ж�������
N=60;
n=20;
%��ֵ
Pth=0.70;
%������¼Ŀǰ���ڼ��ڼ���Ƭ��
Loc=1;
%�洢�������Աȵ��������ݣ�����Ϊn*(N-1)
Normal_Data=data( 1:(n*(N-1)) );
%�����洢���м������ݶΣ�����Ϊn*N
Detect_Data=zeros(1,n*N);
% %f_work��ʾ�Ƿ��������й©���
% f_work=1;
%Acf�洢ÿ��Ƭ�ε�����غ���
Acf=zeros(N,n);
%L_acf�洢����Ƭ�α˴˼�ľ���
Len_Acf=zeros(N,N);
%�����洢Len_Acfÿһ�е�ƽ��ֵ
Len_Acf_Mean=zeros(1,N);
%����������еĴ�������е�Ȩ�أ�������Len_Acf_Mean�����һ��һ��ֵ
Len_Acf_Mean_all=zeros(1,1000);
%����������Normal_Data ת�� ֮��ֵ��Detect_Dataǰn*(N-1)
Detect_Data=Normal_Data';
%�洢�쳣Ƭ�ε�λ��
Res_Loc=[];
Num=1;

%����Ƭ������Ծ���ֻ�����һ�к����һ���ڱ䣬ǰ����ǹ̶��ģ�����д��ѭ������
%.....................��һ��������غ���.........................%    
    %����㷨����һ��������������ÿ��Ƭ�ε�����غ�������N��Ƭ��
for i=1:N-1
    %ȡ��һ��Ƭ��
    x=Detect_Data(1+(i-1)*n : n*i);
    %��ȡ��Ƭ�ε�����غ���
     %��ֹ����Ϊ0������غ���������
    if var(x)==0
        x(2)=x(2)+0.001
    end
    [ACF,lags,bounds]=autocorr(x,n-1);
    %����õ�����غ�����ֵ��Acf�洢
    for j=1:n
        Acf(i,j)=ACF(j);
    end   
end
%.....................�ڶ�����Ƭ�μ�������.....................%
for i=1:N-2
    for j=i+1:N-1
        %����������ˣ�Ȼ���������������ģ�ĳ˻�
        c=dot( Acf(i,:),Acf(j,:) )/( norm(Acf(i,:)) * norm(Acf(j,:)) );
%         C=(Acf(i,:)-Acf(j,:)).^2;
%         c=sqrt(sum(C(:))); 
        Len_Acf(i,j)=c;
        Len_Acf(j,i)=Len_Acf(i,j)
    end
end
% %����ֵ����ΪǰN-1��Ƭ������Ե���Сֵ
% Len_Acf_Mean=mean(Len_Acf);
% Pth=min(Len_Acf_Mean(1:N-1));

%..........................................................................
%............................ѭ���ָ���....................................��
%..........................................................................
%�ںϵ����ݴﵽһ��Ƭ�εĸ����ͽ���һ���ж�
while Loc<=(9990/n-1)
    %��Ŀǰ����Ƭ�μ��뵽������У�����Ϊn
    for i=1:n
       Detect_Data(n*(N-1)+i)=data(n*(Loc-1)+i);
    end
   
%.....................��һ��������غ���.........................%    
%����㷨����һ��������������ÿ��Ƭ�ε�����غ�������N��Ƭ�Σ�ѭ���������N-1��Ƭ��
    %ȡ����N��Ƭ��
    x=Detect_Data(1+(N-1)*n : n*N);
    %��ֹ����Ϊ0������غ���������
    if var(x)==0
        x(1)=x(1)+0.001
    end
    %��ȡ��Ƭ�ε�����غ���
    [ACF,lags,bounds]=autocorr(x,n-1);
    %����õ�����غ�����ֵ��Acf�洢
    for j=1:n
        Acf(N,j)=ACF(j);
    end   
%.....................�ڶ�����Ƭ�μ�������.....................%
    for i=1:N-1
        %����������ˣ�Ȼ���������������ģ�ĳ˻�
        c=dot( Acf(i,:),Acf(N,:) )/( norm(Acf(i,:)) * norm(Acf(N,:)) );
%         C=(Acf(i,:)-Acf(N,:)).^2;
%         c=sqrt(sum(C(:))); 
        Len_Acf(i,N)=c;
        Len_Acf(N,i)=Len_Acf(i,N)
    end
%.....................�������ҳ��쳣���֣������ж�...............%    
    %��Len_Acfÿһ�е�ƽ��ֵ
    Len_Acf_Mean=mean(Len_Acf)*N/(N-1);
    %�����һ�е�ƽ��ֵ��������
    Len_Acf_Mean_all(Loc)=Len_Acf_Mean(N);
    %�жϴ����Ƭ���Ƿ�����
    figure(1);
    if Len_Acf_Mean(N)<Pth
        MMM=mean(Detect_Data(n*(N-1)+1:n*N));
        %if MMM>50
            plot(Loc*n-n/2,1:200,'-r');
            hold on;
             %��¼���Ǹ�Ƭ�����쳣
            Res_Loc(Num)=Loc;
            Num=Num+1;
       % end
    end
    %����Loc
    Loc=Loc+1;
%     %����f_work
%     f_work=f_work+1;
end