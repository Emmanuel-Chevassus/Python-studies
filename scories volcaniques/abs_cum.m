function x = abs_cum(freq_cum, abs_freq_cum, p)
% recherche de l'absisse pour un percentile donné à partir du diag des
% fréq relatives cumulées
% p est soit un scalaire, soit un vecteur contenant les percentiles 
% dont on cherche l'abscisse

% cas1 : p est un scalaire
if (numel(p) == 1)
    % étape1 : trouver les y1 et y2 qui l'encadre
    ind1 = max(find(freq_cum<p));
    ind2 = min(find(freq_cum>p));
    y1 = freq_cum(ind1);
    y2 = freq_cum(ind2);
    
    % étape2 : trouver les x1 et x2 correspondant
    x1 = abs_freq_cum(ind1);
    x2 = abs_freq_cum(ind2);
    
    % étape3 : calculer xp = xp1+(y2-y1)((p-y1)/(y2-y1)) (Thales)
    x = x1 + (x2-x1)*((p-y1)/(y2-y1));
else
    % étape1 : trouver les y1 et y2 qui encadrent chaque quantile
    ind1 = zeros(size(p));
    ind2 = ind1;
    y1 = ind1;
    y2 = ind1;
    for i = 1:length(p),
        ind1(i) = max(find(freq_cum<p(i)));
        ind2(i) = min(find(freq_cum>p(i)));
    end
    y1 = freq_cum(ind1);
    y2 = freq_cum(ind2);
    % étape2 : trouver les x1 et x2 correspondant
    x1 = abs_freq_cum(ind1);
    x2 = abs_freq_cum(ind2);
    % étape3 : calculer xp = xp1+(y2-y1)((p-y1)/(y2-y1)) (Thales)
%     if (size(p, 1) < size(p,2))
%         ind1 = ind1.';
%         ind2 = ind2.';
%         x1 = x1.';
%         x2 = x2.';
%         y1 = y1.';
%         y2 = y2.';
%     end
    x = zeros(size(p));
    for i=1:length(p)
        x(i) = x1(i) + (x2(i)-x1(i))*((p(i)-y1(i))/(y2(i)-y1(i)));
    end
end
    
        
% à vectoriser afin de calculer tous les phi en une passe

