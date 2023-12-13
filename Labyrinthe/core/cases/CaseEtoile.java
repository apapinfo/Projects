package labyrinthe.core.cases;
import labyrinthe.core.objets.*;
import labyrinthe.core.Position;

import java.util.ArrayList;

public class CaseEtoile extends Case
{
    public CaseEtoile()
    {
        super("étoile", new Position(), 0, null, false, false);
    }

    public CaseEtoile(Position position, int rotation, Objet objet, boolean depart, boolean fixe)
    {
        super("étoile", position, rotation, objet, depart, fixe);
    }

    public CaseEtoile(CaseEtoile c)
    {
        super(c);
    }

    public CaseEtoile newInstance()
    {
        CaseEtoile newCase = new CaseEtoile(this);
        return newCase;
    }

    @Override
    public String afficher()
    {
            return "*";
    }

    @Override
    public ArrayList<Position> getDeplacement() 
    {
        ArrayList<Position> deplacementpossible = new ArrayList<Position>();

        // -
        deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur())); // à gauche
        deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.position.getHauteur())); // à droite

        // |
        deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() - 1)); // en haut
        deplacementpossible.add(new Position(this.position.getLongueur(), this.position.getHauteur() + 1)); // en bas

        // /
        deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur() + 1)); // bas gauche
        deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.getPosition().getHauteur() - 1)); // haut droit

        // \
        deplacementpossible.add(new Position(this.position.getLongueur() - 1, this.position.getHauteur() - 1)); // haut gauche
        deplacementpossible.add(new Position(this.position.getLongueur() + 1, this.getPosition().getHauteur() + 1)); // bas droit

        return deplacementpossible;
    }
    
    @Override
    public boolean equals(Object o)
    {
        if (o instanceof CaseEtoile == false)
            return false;
        else
        {
            CaseEtoile caseEtoile = (CaseEtoile) o;
            return this.toString().equals(caseEtoile.toString());
        }
    }
}