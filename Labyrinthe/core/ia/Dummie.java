package labyrinthe.core.ia;

import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;

import labyrinthe.core.Joueur;
import labyrinthe.core.Plateau;
import labyrinthe.core.Position;
import labyrinthe.core.cases.Case;

public class Dummie extends Ia
{
    public Dummie()
    {
        super();
    }

    public int rotationCase(Case c)
    {
        int randomRotation = ThreadLocalRandom.current().nextInt(0,4);
        int rotation = 0;
        switch (randomRotation)
        {
            case 1:
                rotation = 0;
                break;
            case 2:
                rotation = 90;
            case 3:
                rotation = 180;
            case 4:
                rotation = 270;
        }

        return rotation;
    }

    public Position deplacementCase(Plateau plateau, Joueur joueur)
    {
        ArrayList<Position> listeDeplacementCase = new ArrayList<>();
        for (int i = 1; i < plateau.getLongueur(); i+=2)
        {
            listeDeplacementCase.add(new Position(i, -1));
            listeDeplacementCase.add(new Position(i, plateau.getHauteur()));
        }
        for (int i = 1; i < plateau.getHauteur(); i+=2)
        {
            listeDeplacementCase.add(new Position(-1, i));
            listeDeplacementCase.add(new Position(plateau.getLongueur(), i));
        }

        int random = ThreadLocalRandom.current().nextInt(0, listeDeplacementCase.size()); 

        System.out.println("[DEBUG]: Case = " + listeDeplacementCase.get(random));
        return listeDeplacementCase.get(random);
    }

    public Position deplacementJoueur(Plateau plateau, Joueur joueur)
    {
        ArrayList<Position> listeDeplacementJoueur = joueur.getToutDeplacementPossible(plateau.getPlateau());

        if (!joueur.recupererToutObjet())
        {
            Position positionCaseAchercher = plateau.rechercherCase(joueur.getPaquetCarte().get(0)).getPosition();
            for (int i = 0; i < listeDeplacementJoueur.size(); i++)
                if (listeDeplacementJoueur.get(i) == positionCaseAchercher)
                    return listeDeplacementJoueur.get(i);
        }
        else
        {
            for (int i = 0; i < listeDeplacementJoueur.size(); i++)
                if (listeDeplacementJoueur.get(i) == plateau.getPositionDepartJoueur().get(joueur))
                    return listeDeplacementJoueur.get(i);
        }

        if (listeDeplacementJoueur.size() > 0)
        {
            int random = ThreadLocalRandom.current().nextInt(0, listeDeplacementJoueur.size());
            return listeDeplacementJoueur.get(random);
        }
        else
            return joueur.getPosition();
    }
}
