clear; close all; clc;
%% Importing Data
audioFeatures = readtable('audioFeatures.csv');
trackInfo = readtable('trackInfo.csv');
trackInfo(:,1) = [];
pat = lettersPattern;
genreTags = table2cell(trackInfo(:,3));

genreList = ["Classical" , "80s" , "Hip Hop" , "Metal"];
songs = [1:height(audioFeatures)];
numGenres = 4;
songsPerGenre = songs(end)/numGenres;
songMean = zeros(numGenres,1);
average = zeros(numGenres,1);
%organizing labels/data
audioFeaturesLabels = extract(string(table2cell(audioFeatures(1,1:2:width(audioFeatures)/2))),pat);

audioFeaturesData = audioFeatures(:,2:2:width(audioFeatures)/2);

pitchTimbre = cell(height(audioFeatures),2);
audioFeaturesDataNew = zeros(height(audioFeatures),width(audioFeaturesData));
for i = 1:height(audioFeatures)
    for j = 1 : width(audioFeaturesData)
        audioFeaturesDataNew(i,j) = str2num(cell2mat(table2array(audioFeaturesData(i,j))));
        if (i ==1) audioFeaturesLabels{j}(1) = upper(audioFeaturesLabels{j}(1)); 
        end
    end
end
%% Plotting
for i = 1:width(audioFeaturesData)
    figure(i)
        for j = 1:numGenres
            genreSection = [(songsPerGenre*j-songsPerGenre+1):songsPerGenre*j];
            songMean(j) = mean(genreSection);
            average(j) = mean(audioFeaturesDataNew(genreSection,i));
            scatter(songs(genreSection),audioFeaturesDataNew(genreSection,i),50,'filled')
            hold on 
            audioFeat4{i}(:,j) = audioFeaturesDataNew(genreSection,i);
        end
    plot(songMean,average,'--k.','Linewidth',2','Markersize',34)
    hold on
    grid on
    xlabel('Song Genres')
    title('Audio Feature by Genre')
    ylabel(audioFeaturesLabels{i})
    if (i ==2 || i ==4) location = 'Southeast';
    else location = 'Northeast';end
    legend(["Classical" , "80s" , "Hip Hop" , "Metal"],'Location',location)
end

Dancibility = audioFeat4{1};
Energy = audioFeat4{2};
Key = audioFeat4{3};
Loudness = audioFeat4{4};
mode = audioFeat4{5};
Speechiness = audioFeat4{6};
Acousticness = audioFeat4{7};
Instrumentalness = audioFeat4{8};
Liveness = audioFeat4{9};

audioFeaturesDataSet = [Dancibility;Energy;Loudness;Speechiness;Acousticness;Instrumentalness];

for i = 1:width(audioFeaturesData)
    figure(width(audioFeaturesData)+i)
    boxplot(audioFeat4{i},genreList)
    title('Audio Feature by Genre')
    hold on
    grid on
    xlabel('Song Genres')
    ylabel(audioFeaturesLabels{i})
end