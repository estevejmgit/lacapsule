describe("General Scripts", () => {
    beforeEach(() => {
        cy.visit("https://www.booking.com");
    })
    it("getSearchFocus", () => {
        cy.wait(5000);
        // cy.get("input#search").type("DevOps");
        cy.get("button.dc0e35d124 > span:nth-child(1) > span:nth-child(1) > svg:nth-child(1) > path:nth-child(1)").click();
        cy.get("#\\:r8\\:").type("londres");
        cy.get("#indexsearch > div.hero-banner-searchbox > div > form > div.beb79c8078.cf33f513d7.b61f645dc6 > div:nth-child(2) > div > div.b90aaa8bb3 > button:nth-child(2) > span").click();
        cy.wait(1000);
        cy.get("button.dc0e35d124").click();
        cy.get("button.dc0e35d124:nth-child(2)").click();
         // Boucle pour aller a decembre
        for (let i = 0; i < 4; i++) {
            cy.get("button.dc0e35d124:nth-child(2)").click();
            cy.wait(500);
        }
        // click 31 dec
        cy.get('[data-date="2024-12-31"]').click();
        cy.get('[data-date="2025-01-01"]').click();
        cy.get("button.c73e91a7c9").click();
        //cy.get("div.c8ea4584c4:nth-child(1) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(6) > td:nth-child(2) > span:nth-child(1) > span:nth-child(1)").click();
        // click 1er Jan
        //cy.get("div.c8ea4584c4:nth-child(2) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)").click();
        // cy.get("#indexsearch > div.hero-banner-searchbox > div > form > div.beb79c8078.cf33f513d7.b61f645dc6 > div.be95eea937.c4255fc1c2 > button").click();
        // cy.get("li.option:nth-child(21)").click();
        // cy.get("input#search").type("DevOps");   
        // cy.wait(500);
        // cy.get("select#lang").select("Wallon");
        // cy.wait(500);
        // cy.contains("Wallon").click();
        // cy.contains("DevOps");
        // cy.get("select#lang").select("wa");
        // cy.get("select#lang").wait(500).select("Wallon");
        //   document.querySelector("")
        // cy.get("select#lang").wait(5).select("wa");   
    })
})