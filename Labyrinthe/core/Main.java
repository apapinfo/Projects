package labyrinthe.core;
import labyrinthe.core.cases.*;
import labyrinthe.core.ia.Dummie;
import labyrinthe.core.objets.*;
import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;
import java.util.Scanner;
    
    public class Main 
    {
        public static void main(String[] args)
        {
            Scanner scanner = new Scanner(System.in);

            ArrayList<Objet> listeObjet = new ArrayList<Objet>();
            Araignee araignee = new Araignee();
            listeObjet.add(araignee);
            Bague bague = new Bague();
            listeObjet.add(bague);
            Bourse bourse = new Bourse();
            listeObjet.add(bourse);
            CarteTresor carteTresor = new CarteTresor();
            listeObjet.add(carteTresor);
            Chandelier chandelier = new Chandelier();
            listeObjet.add(chandelier);
            ChauveSouris chauveSouris = new ChauveSouris();
            listeObjet.add(chauveSouris);
            CoffreTresor coffreTresor = new CoffreTresor();
            listeObjet.add(coffreTresor);
            Couronne couronne = new Couronne();
            listeObjet.add(couronne);
            Crane crane = new Crane();
            listeObjet.add(crane);
            Dragon dragon = new Dragon();
            listeObjet.add(dragon);
            Emeraude emeraude = new Emeraude();
            listeObjet.add(emeraude);
            Encyclopedie encyclopedie = new Encyclopedie();
            listeObjet.add(encyclopedie);
            Epee epee = new Epee();
            listeObjet.add(epee);
            EspritFarceur espritFarceur = new EspritFarceur();
            listeObjet.add(espritFarceur);
            Fantome fantome = new Fantome();
            listeObjet.add(fantome);
            Heaume heaume = new Heaume();
            listeObjet.add(heaume);
            Hibou hibou = new Hibou();
            listeObjet.add(hibou);
            Hobbit hobbit = new Hobbit();
            listeObjet.add(hobbit);
            Magicienne magicienne = new Magicienne();
            listeObjet.add(magicienne);
            PapillonDeNuit papillonDeNuit = new PapillonDeNuit();
            listeObjet.add(papillonDeNuit);
            Rat rat = new Rat();
            listeObjet.add(rat);
            Salamandre salamandre = new Salamandre();
            listeObjet.add(salamandre);
            Scarabee scarabee = new Scarabee();
            listeObjet.add(scarabee);
            Trousseau trousseau = new Trousseau();
            listeObjet.add(trousseau);

            ArrayList<Joueur> listeJoueurs = new ArrayList<>();
            System.out.println("Entrez le nom du joueur : ");
            while (scanner.hasNext())
            {
                String nom = scanner.next();
                if (nom.equals("fin"))
                    break;
                else
                {
                    Joueur j;
                    if (nom.equals("Dummie"))
                        j = new Joueur(nom, null, new Dummie());
                    else
                        j = new Joueur(nom, null);

                    listeJoueurs.add(j);
                    System.out.println("Entrez le nom du joueur : ");  
                }
            }

            ArrayList<Objet> listeToutObjet = new ArrayList<Objet>(listeObjet);
            for (int i = 0; i < listeJoueurs.size(); i++)
                for (int j = 0; j < (int) (listeObjet.size() / listeJoueurs.size()); j++)
                {
                    int randomObjet = ThreadLocalRandom.current().nextInt(0,listeToutObjet.size());
                    listeJoueurs.get(i).addObjet(listeToutObjet.get(randomObjet));
                    listeToutObjet.remove(randomObjet);
                }
            

            ArrayList<Case> listeCase = new ArrayList<>();
            ArrayList<Integer> nbCases = new ArrayList<>();
            // Plateau par défaut   
            listeCase.add(new CaseLigne());
            nbCases.add(12);

            listeCase.add(new CaseCoude());
            nbCases.add(20);

            listeCase.add(new CaseT());
            nbCases.add(18);

            ArrayList<Case> cases = new ArrayList<Case>();

            for (int i = 0; i < nbCases.size(); i++)
                for (int j = 0; j < nbCases.get(i); j++)
                    cases.add(listeCase.get(i));

            // Plateau moddé (exemple)
            /*listeCase.add(new CaseCoude());
            nbCases.add(12);
            listeCase.add(new CaseDiagonale());
            nbCases.add(13);
            listeCase.add(new CaseEtoile());
            nbCases.add(13);
            listeCase.add(new CaseFois());
            nbCases.add(13);
            listeCase.add(new CaseLigne());
            nbCases.add(13);
            listeCase.add(new CaseMur());
            nbCases.add(12);
            listeCase.add(new CasePlus());
            nbCases.add(13);
            listeCase.add(new CaseT());
            nbCases.add(12); 
            
            ArrayList<Case> cases = new ArrayList<Case>();

            for (int i = 0; i < nbCases.size(); i++)
                for (int j = 0; j < nbCases.get(i); j++)
                    cases.add(listeCase.get(i));*/

            Plateau plateau = new Plateau(listeJoueurs, cases, listeObjet);
            //Plateau plateau = new Plateau(listeJoueurs, 10, 10, cases, listeObjet);

            while (!plateau.finPartie())
            {
                for (int i = 0; i < listeJoueurs.size(); i++)
                {
                    var caseDefaussee = plateau.getCaseDefaussee();
                    System.out.println(listeJoueurs.get(i));
                    System.out.println(plateau);
                    System.out.println(caseDefaussee);
                    if (listeJoueurs.get(i).getPaquetCarte().size() > 0)
                        System.out.println("Objet à trouver: " + listeJoueurs.get(i).getPaquetCarte().get(0).getNom() + " et sa Position : " + plateau.rechercherCase(listeJoueurs.get(i).getPaquetCarte().get(0)).getPosition() + "\n");
                    else
                        System.out.println("Tout les objets ont été trouvé, veuillez retourner à votre point de départ");

                    if (listeJoueurs.get(i).getIa() == null)
                    {
                        boolean deplacementCase = false;
                        while(!deplacementCase)
                        {
                            System.out.println("Entrez rotation, x, y");
                            int rotation = scanner.nextInt();
                            int x = scanner.nextInt();
                            int y = scanner.nextInt();

                            caseDefaussee.setRotation(rotation);
                            caseDefaussee.setPosition(new Position(x,y));
                            if (plateau.deplacerCase(caseDefaussee))
                                deplacementCase = true;
                            else
                                System.out.println("déplacement case impossible");
                        }

                        System.out.println(plateau);

                        boolean deplacementJoueur = false;
                        while(!deplacementJoueur)
                        {
                            System.out.println(listeJoueurs.get(i).getToutDeplacementPossible(plateau.getPlateau()));
                        
                            System.out.println("Entrez x, y");
                            int x = scanner.nextInt();
                            int y = scanner.nextInt();

                            if (listeJoueurs.get(i).deplacer(plateau.getPlateau(), new Position(x,y)))
                                deplacementJoueur = true;
                            else
                                System.out.println("déplacement joueur impossible");
                        }
                    }
                    else
                    {
                        int waitTime = 0;

                        System.out.println("[IA] Déplacement case...");
                        try {
                            Thread.sleep(waitTime);
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                        int rCase = listeJoueurs.get(i).getIa().rotationCase(null); 
                        Position depCase = listeJoueurs.get(i).getIa().deplacementCase(plateau, listeJoueurs.get(i));
                        caseDefaussee.setRotation(rCase);
                        caseDefaussee.setPosition(depCase);
                        plateau.deplacerCase(caseDefaussee);

                        System.out.println(plateau);

                        System.out.println("[IA]: Déplacement joueur...");
                        try {
                            Thread.sleep(waitTime);
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                        Position depJoueur = listeJoueurs.get(i).getIa().deplacementJoueur(plateau, listeJoueurs.get(i));
                        listeJoueurs.get(i).deplacer(plateau.getPlateau(), depJoueur);

                        System.out.println(plateau);
                    }
                    

                    plateau.joueurRecupereObjet(listeJoueurs.get(i));
                    
                    if (listeJoueurs.get(i).recupererToutObjet() && listeJoueurs.get(i).getPosition() == plateau.getPositionDepartJoueur().get(listeJoueurs.get(i))) {
                        System.out.println(listeJoueurs.get(i).getNom() + " à gagné !");
                        break;  
                    }                  
                }
            }

            scanner.close();
        }  
    }
