package labyrinthe.core;
import labyrinthe.core.cases.*;
import labyrinthe.core.objets.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.concurrent.ThreadLocalRandom;

public class Plateau 
{
    private int longueur, hauteur;
    private ArrayList<Joueur> listeJoueur = new ArrayList<Joueur>();
    private ArrayList<Case> plateau = new ArrayList<Case>();
    private HashMap<Joueur, Position> positionDepartJoueur = new HashMap<>();
    private Case caseDefaussee;
    private Position positionCaseInterdite;

    // utile uniquement pour le terminal
    public static final String ANSI_RESET = "\u001B[0m";

    public Plateau(ArrayList<Case> cases, ArrayList<Objet> listeObjet)
    {
        this.longueur = 7; this.hauteur = 7;

        for (int i = 0; i < 4; i++)
            this.listeJoueur.add(new Joueur());
        
        this.plateau = creationPlateau(cases);
        this.positionCaseInterdite = new Position(0,0);
        
        positionDepart();
    }

    public Plateau(ArrayList<Joueur> listeJoueurs, ArrayList<Case> cases, ArrayList<Objet> listeObjet)
    {
        this.longueur = 7; this.hauteur = 7;
        this.listeJoueur = listeJoueurs;
        this.plateau = creationPlateau(cases);
        this.positionCaseInterdite = new Position(0,0);

        positionDepart();
    }

    public Plateau(ArrayList<Joueur> listeJoueurs, int longueur, int hauteur, ArrayList<Case> cases, ArrayList<Objet> listeObjet)
    {
        this.longueur = longueur; this.hauteur = hauteur;
        this.listeJoueur = listeJoueurs;
        this.plateau = creationPlateauMod(cases, listeObjet);
        this.positionCaseInterdite = new Position(0,0);

        positionDepart();
    }

    // get plateau (pour joueur)
    public ArrayList<Case> getPlateau()
    {
        return this.plateau;
    }

    public HashMap<Joueur, Position> getPositionDepartJoueur()
    {
        return this.positionDepartJoueur;
    }

    public Case getCaseDefaussee()
    {
        return this.caseDefaussee;
    }

    public ArrayList<Joueur> getListeJoueur()
    {
        return this.listeJoueur;
    }

    public int getLongueur() 
    {
        return this.longueur;
    }

    public int getHauteur() 
    {
        return this.hauteur;
    }

    // création d'un plateau standard
    private ArrayList<Case> creationPlateau(ArrayList<Case> listeCase)
    {
        ArrayList<Case> p = new ArrayList<Case>();

        for (int i = 0; i < 4; i++)
        {
            var casedepart = listeCase.get(listeCase.indexOf(new CaseCoude())).newInstance();
            listeCase.remove(casedepart);
            switch (i)
            {
                case 0:
                    casedepart.setPosition(new Position(0,0));
                    casedepart.setRotation(180);
                    break;
                case 1:
                    casedepart.setPosition(new Position(this.longueur -1, 0));
                    casedepart.setRotation(270);
                    break;
                case 2:
                    casedepart.setPosition(new Position(0, this.hauteur -1));
                    casedepart.setRotation(90);
                    break;
                case 3:
                    casedepart.setPosition(new Position(this.longueur -1, this.hauteur -1));
                    casedepart.setRotation(0);
                    break;
            }
            casedepart.setDepart(true);
            casedepart.setFixe(true);

            p.add(casedepart);
        }

        for (int i = 0; i < 12; i++)
        {
            var caseFixe = listeCase.get(listeCase.indexOf(new CaseT())).newInstance();
            listeCase.remove(caseFixe);
            switch (i)
            {
                case 0:
                    caseFixe.setPosition(new Position(2,0));
                    caseFixe.setRotation(270);
                    caseFixe.setObjet(new Crane());
                    break;

                case 1:
                    caseFixe.setPosition(new Position(4,0));
                    caseFixe.setRotation(270);
                    caseFixe.setObjet(new Epee());
                    break;

                case 2:
                    caseFixe.setPosition(new Position(0,2));
                    caseFixe.setRotation(180);
                    caseFixe.setObjet(new Bourse());
                    break;

                case 3:
                    caseFixe.setPosition(new Position(2,2));
                    caseFixe.setRotation(180);
                    caseFixe.setObjet(new Trousseau());
                    break;
                
                case 4:
                    caseFixe.setPosition(new Position(4,2));
                    caseFixe.setRotation(270);
                    caseFixe.setObjet(new Emeraude());
                    break;
                
                case 5:
                    caseFixe.setPosition(new Position(6,2));
                    caseFixe.setRotation(0);
                    caseFixe.setObjet(new Heaume());
                    break;

                case 6:
                    caseFixe.setPosition(new Position(0,4));
                    caseFixe.setRotation(180);
                    caseFixe.setObjet(new Encyclopedie());
                    break;

                case 7:
                    caseFixe.setPosition(new Position(2,4));
                    caseFixe.setRotation(90);
                    caseFixe.setObjet(new Couronne());
                    break;

                case 8:
                    caseFixe.setPosition(new Position(4,4));
                    caseFixe.setRotation(0);
                    caseFixe.setObjet(new CoffreTresor());
                    break;

                case 9:
                    caseFixe.setPosition(new Position(6,4));
                    caseFixe.setRotation(0);
                    caseFixe.setObjet(new Chandelier());
                    break;
                
                case 10:
                    caseFixe.setPosition(new Position(2,6));
                    caseFixe.setRotation(90);
                    caseFixe.setObjet(new CarteTresor());
                    break;
                
                case 11:
                    caseFixe.setPosition(new Position(4,6));
                    caseFixe.setRotation(90);
                    caseFixe.setObjet(new Bague());
                    break;
            }
            caseFixe.setFixe(true);
            p.add(caseFixe);

        }


        while (listeCase.size() > 0)
        {
            int randomCase = ThreadLocalRandom.current().nextInt(0,listeCase.size()); 
            var caseRandom = listeCase.get(randomCase).newInstance();
            listeCase.remove(caseRandom);

            ArrayList<Position> positionRestantes = getPositionCasePlateau(p);
            if (positionRestantes.size() > 0)
            {
                caseRandom.setPosition(positionRestantes.get(0));
                setRandomRotationCase(caseRandom);
                p.add(caseRandom);
            }
            else
                this.caseDefaussee = caseRandom;
        }

        ArrayList<Objet> listeObjet = new ArrayList<>();
        listeObjet.add(new Salamandre());
        listeObjet.add(new Fantome());
        listeObjet.add(new Scarabee());
        listeObjet.add(new Magicienne());
        listeObjet.add(new Hobbit());
        listeObjet.add(new Araignee());
        listeObjet.add(new PapillonDeNuit());
        listeObjet.add(new Hibou());
        listeObjet.add(new EspritFarceur());
        listeObjet.add(new Rat());
        listeObjet.add(new ChauveSouris());
        listeObjet.add(new Dragon());

        while (listeObjet.size() > 0)
        {
            for (int i = 0; i < p.size(); i++)
                if (p.get(i).getObjet() == null && !p.get(i).getFixe())
                {
                    int avoirObjet = ThreadLocalRandom.current().nextInt(0,2);
                    if (avoirObjet == 1)
                    {
                        if (listeObjet.size() > 0)
                        {
                            int randomObjet = ThreadLocalRandom.current().nextInt(0,listeObjet.size());
                            p.get(i).setObjet(listeObjet.get(randomObjet));
                            listeObjet.remove(randomObjet);
                        }                      
                    } 
                }
        }

        return p;
    }

    // plateau moddé
    private ArrayList<Case> creationPlateauMod(ArrayList<Case> listeCase, ArrayList<Objet> listeObjet)
    {
        ArrayList<Case> p = new ArrayList<Case>();

        for (int i = 0; i < this.listeJoueur.size(); i++) {
            int randomCase = ThreadLocalRandom.current().nextInt(0, listeCase.size());
            var caseDepart = listeCase.get(randomCase);
            listeCase.remove(randomCase);

            caseDepart.setDepart(true);
            caseDepart.setFixe(true);

            setRandomRotationCase(caseDepart);
            setPositionDepart(caseDepart, i);

            p.add(caseDepart.newInstance());
        }

        while (listeCase.size() > 0) {
            int randomCase = ThreadLocalRandom.current().nextInt(0,listeCase.size()); 
            var caseRandom = listeCase.get(randomCase).newInstance();
            listeCase.remove(caseRandom);

            ArrayList<Position> positionRestantes = getPositionCasePlateau(p);

            if (positionRestantes.size() > 0) {
                caseRandom.setDepart(false);
                caseRandom.setFixe(false);
                caseRandom.setPosition(positionRestantes.get(0));
                setRandomRotationCase(caseRandom);
                p.add(caseRandom);
            }
            else
                this.caseDefaussee = caseRandom;
        }

        // set case fixe sur le plateau
        for (int i = 0; i < this.longueur; i += 2)
            for (int j = 0; j < this.hauteur; j += 2)
            {
                int k = 0;
                boolean caseFixe = false;
                while (!caseFixe)
                {
                    if (p.get(k).getPosition().equals(new Position(i, j)))
                    {
                        p.get(k).setFixe(true);
                        caseFixe = true;
                    }
                    k++;
                }
            }
            
        // set objet sur le plateau
        while (listeObjet.size() > 0)
        {
            for (int i = 0; i < p.size(); i++)
                if (p.get(i).getObjet() == null && !p.get(i).getFixe())
                {
                    int avoirObjet = ThreadLocalRandom.current().nextInt(0,2);
                    if (avoirObjet == 1)
                    {
                        if (listeObjet.size() > 0)
                        {
                            int randomObjet = ThreadLocalRandom.current().nextInt(0,listeObjet.size());
                            p.get(i).setObjet(listeObjet.get(randomObjet));
                            listeObjet.remove(randomObjet);
                        }                      
                    } 
                }
        }

        return p;
    }

    // permet de savoir les positions qui ne sont pas déjà utilisé
    private ArrayList<Position> getPositionCasePlateau(ArrayList<Case> p) {
        ArrayList<Position> positionCasePlateau = new ArrayList<Position>();
        
        for (int x = 0; x < this.longueur; x++)
            for (int y = 0; y < this.hauteur; y++)
                positionCasePlateau.add(new Position(x, y));
            
        for (int i = 0; i < p.size(); i++)
            if (positionCasePlateau.contains(p.get(i).getPosition()))
                positionCasePlateau.remove(p.get(i).getPosition());
        
        return positionCasePlateau;
            
    }

    private void setRandomRotationCase(Case c)
    {
        int randomRotation = ThreadLocalRandom.current().nextInt(0,4);
        switch (randomRotation)
        {
            case 1:
                c.setRotation(0);
                break;
            case 2:
                c.setRotation(90);
            case 3:
                c.setRotation(180);
            case 4:
                c.setRotation(270);
        }
    }

    // j'ai pas trouvé de solution pour toute les possibilité
    private void setPositionDepart(Case caseDepart, int index) {
        switch (index) {
            case 0:
                caseDepart.setPosition(new Position(0,0));
                break;
            case 1:
                caseDepart.setPosition(new Position(this.longueur -1, 0));
                break;
            case 2:
                caseDepart.setPosition(new Position(0, this.hauteur -1));
                break;
            case 3:
                caseDepart.setPosition(new Position(this.longueur -1, this.hauteur -1));
                break;
        }
    }

    private void positionDepart()
    {
        int indexJoueur = 0;
        for (int i = 0; i < this.plateau.size(); i++)
            if (indexJoueur < this.listeJoueur.size())
                if (plateau.get(i).getDepart())
                {
                    this.listeJoueur.get(indexJoueur).setPosition(plateau.get(i).getPosition());
                    positionDepartJoueur.put(this.listeJoueur.get(indexJoueur), plateau.get(i).getPosition());
                    indexJoueur++;
                }
    }

    public Case rechercherCase(Objet objet)
    {
        for (int i = 0; i < plateau.size(); i++)
            if (plateau.get(i).getObjet() != null)
                if (plateau.get(i).getObjet().equals(objet))
                    return plateau.get(i);

        if (this.caseDefaussee.getObjet().equals(objet))
            return this.caseDefaussee;

        return null;
    }

    public boolean deplacerCase(Case c)
    {
        // PS : la case qui sera rajouté sera dans une position "impossible" Position(-1,0) pour savoir le sens de déplacement si on veut deplacer dans les coins
        if ((c.getPosition().getLongueur() == -1 || c.getPosition().getLongueur() == this.longueur) && (c.getPosition().getHauteur() >= 0 && c.getPosition().getHauteur() < this.hauteur) || (c.getPosition().getHauteur() == -1 || c.getPosition().getHauteur() == this.hauteur) && (c.getPosition().getLongueur() >= 0 && c.getPosition().getLongueur() < this.longueur))
        {

            int deplacementX = 0; int deplacementY = 0; // sens de déplacement des cases

            // please corriger ça, c'est *m o c h e*
            if (c.getPosition().getLongueur() == -1)
                deplacementX = 1;
            else 
                if (c.getPosition().getLongueur() == this.longueur)
                    deplacementX = -1;

            if (c.getPosition().getHauteur() == -1)
                deplacementY = 1;
            else 
                if (c.getPosition().getHauteur() == this.hauteur)
                    deplacementY = -1;

            if (positionCaseInterdite.getLongueur() == -1)
                positionCaseInterdite.setLongueur(this.longueur);
            else
                if (positionCaseInterdite.getLongueur() == this.longueur)
                    positionCaseInterdite.setLongueur(-1);
            
            if (positionCaseInterdite.getHauteur() == -1)
                positionCaseInterdite.setHauteur(this.hauteur);
            else
                if (positionCaseInterdite.getHauteur() == this.hauteur)
                    positionCaseInterdite.setHauteur(-1);
            
            if (c.getPosition().equals(positionCaseInterdite))
                return false;
                

            if (checkDeplacementCase(c.getPosition()) != null)
            {
                ArrayList<Case> listeCaseADeplacer = checkDeplacementCase(c.getPosition());
                for (int i = 0; i < listeCaseADeplacer.size(); i++)
                {
                    if (listeCaseADeplacer.get(i).getPosition().getLongueur() + deplacementX < 0 || listeCaseADeplacer.get(i).getPosition().getLongueur() + deplacementX >= this.longueur || listeCaseADeplacer.get(i).getPosition().getHauteur() + deplacementY < 0 || listeCaseADeplacer.get(i).getPosition().getHauteur() + deplacementY >= this.hauteur) // ça fait beaucoup là non ? xd
                    {
                        this.caseDefaussee = listeCaseADeplacer.get(i);
                        this.caseDefaussee.setPosition(null);                       
                        this.plateau.remove(listeCaseADeplacer.get(i));
                    }
                    else
                    {
                        int nouveauX = plateau.get(plateau.indexOf(listeCaseADeplacer.get(i))).getPosition().getLongueur() + deplacementX;
                        int nouveauY = plateau.get(plateau.indexOf(listeCaseADeplacer.get(i))).getPosition().getHauteur() + deplacementY;
                        plateau.get(plateau.indexOf(listeCaseADeplacer.get(i))).setPosition(new Position(nouveauX, nouveauY));
                    }
                }

                this.positionCaseInterdite = c.getPosition();

                ArrayList<Case> ancienneListeCaseADeplacer = new ArrayList<Case>(checkDeplacementCase(c.getPosition()));
                int nouveauXCase = c.getPosition().getLongueur();
                int nouveauYCase = c.getPosition().getHauteur();
                c.setPosition(new Position(nouveauXCase + deplacementX, nouveauYCase + deplacementY));
                plateau.add(c);

                deplacementJoueur(ancienneListeCaseADeplacer, deplacementX, deplacementY, c.getPosition());
            }
            else
                return false;        
        }
        else
            return false;
        
        return true;
    }

    //  liste des cases à déplacer (null si impossible)
    private ArrayList<Case> checkDeplacementCase(Position p)
    {
        ArrayList<Case> listeCase = new ArrayList<Case>();

        for (int i = 0; i < this.plateau.size(); i++)
        {
            if (p.getLongueur() == -1 || p.getLongueur() == this.longueur)
                if (this.plateau.get(i).getPosition().getHauteur() == p.getHauteur())
                    listeCase.add(this.plateau.get(i));

            if (p.getHauteur() == -1 || p.getHauteur() == this.hauteur)
                if (this.plateau.get(i).getPosition().getLongueur() == p.getLongueur())
                    listeCase.add(this.plateau.get(i));
        }

        boolean caseFixe = false;
        for (int j = 0; j < listeCase.size(); j++)
            if (listeCase.get(j).getFixe())
                caseFixe = true;

        if (caseFixe)
            listeCase = null;
            
        return listeCase;
    }

    private void deplacementJoueur(ArrayList<Case> listeCaseADeplacer, int deplacementX, int deplacementY, Position nouvellePosition)
    {
        ArrayList<Joueur> joueurADeplacer = new ArrayList<Joueur>(this.listeJoueur);
        for (int i = 0; i < listeCaseADeplacer.size(); i++)
            for (int j = 0; j < joueurADeplacer.size(); j++)
            {
                if (joueurADeplacer.get(j).getPosition().getLongueur() == listeCaseADeplacer.get(i).getPosition().getLongueur() && joueurADeplacer.get(j).getPosition().getHauteur() == listeCaseADeplacer.get(i).getPosition().getHauteur())
                {
                    if (joueurADeplacer.get(j).getPosition().getLongueur() + deplacementX < 0 || joueurADeplacer.get(j).getPosition().getLongueur() + deplacementX >= this.longueur || joueurADeplacer.get(j).getPosition().getHauteur() + deplacementY < 0 || joueurADeplacer.get(j).getPosition().getHauteur() + deplacementY >= this.hauteur)
                        joueurADeplacer.get(j).setPosition(nouvellePosition);
                    else
                        joueurADeplacer.get(j).setPosition(new Position(joueurADeplacer.get(j).getPosition().getLongueur() + deplacementX, joueurADeplacer.get(j).getPosition().getHauteur() + deplacementY));

                    joueurADeplacer.remove(j);
                }
                else if (joueurADeplacer.get(j).getPosition().getLongueur() == listeCaseADeplacer.get(i).getPosition().getLongueur() -deplacementX && joueurADeplacer.get(j).getPosition().getHauteur() == listeCaseADeplacer.get(i).getPosition().getHauteur() - deplacementY)
                {
                    if (joueurADeplacer.get(j).getPosition().getLongueur() + deplacementX < 0 || joueurADeplacer.get(j).getPosition().getLongueur() + deplacementX >= this.longueur || joueurADeplacer.get(j).getPosition().getHauteur() + deplacementY < 0 || joueurADeplacer.get(j).getPosition().getHauteur() + deplacementY >= this.hauteur)
                        joueurADeplacer.get(j).setPosition(nouvellePosition);
                    else
                        joueurADeplacer.get(j).setPosition(new Position(joueurADeplacer.get(j).getPosition().getLongueur() + deplacementX, joueurADeplacer.get(j).getPosition().getHauteur() + deplacementY));

                    joueurADeplacer.remove(j);
                } 
            }   
    }

    public void joueurRecupereObjet(Joueur j)
    {
        for (int i = 0; i < this.plateau.size(); i++)
            if (plateau.get(i).getObjet() != null)
                if (this.plateau.get(i).getPosition().equals(j.getPosition()))
                    if (j.getPaquetCarte().size() > 0)
                        if (this.plateau.get(i).getObjet().getNom().equals(j.getPaquetCarte().get(0).getNom()))
                            j.aRecupererObjet();
    }

    public Boolean finPartie()
    {
        boolean fini = false;
        for (int i = 0; i < this.listeJoueur.size(); i++)
            if (this.listeJoueur.get(i).recupererToutObjet() && this.listeJoueur.get(i).getPosition() == this.positionDepartJoueur.get(this.listeJoueur.get(i)))
                fini = true;
        
        return fini;
    }
    
    @Override
    public String toString()
    {
        // affiche 0 1 2 3 4 [...] this.longueur \n
        String contenu = "";
        for (int i = 0; i < this.longueur; i++)
            contenu += i + " ";
        contenu += "\n";

        ArrayList<Case> copyPlateau = new ArrayList<>(this.plateau);
        int x = 0; int y = 0;
        while (copyPlateau.size() > 0)
        {
            for (int i = 0; i < copyPlateau.size(); i++) {
                if (y > this.hauteur)
                    System.out.println("[DEBUG]: x = " + x + " y = " + y);
                if (copyPlateau.get(i).getPosition().equals(new Position(x,y)))
                {
                    // pour les couleurs sur le plateau
                    String couleur = "\u001B[37m"; // blanc
                    String background = ANSI_RESET;
                    for (int j = 0; j < this.listeJoueur.size(); j++) {
                        if (copyPlateau.get(i).getPosition().equals(this.listeJoueur.get(j).getPosition()))
                            couleur = this.listeJoueur.get(j).getCouleur();
                        if (copyPlateau.get(i).getObjet() != null)
                            if (this.listeJoueur.get(j).getPaquetCarte().size() != 0)
                                if (copyPlateau.get(i).getObjet().getNom().equals(this.listeJoueur.get(j).getPaquetCarte().get(0).getNom()))
                                    background = this.listeJoueur.get(j).getCouleurFond();
                    }
                    contenu += background + couleur + copyPlateau.get(i).afficher() + ANSI_RESET + " ";
                    copyPlateau.remove(i);
                }
            }

            if (x < this.longueur - 1)
                x++;
            else
                if (x == this.longueur - 1)
                {
                    contenu += y + "\n";
                    x = 0; y++;
                    if (y > this.hauteur)
                        y = 0;
                }
        }      

        return contenu;
    }   
}