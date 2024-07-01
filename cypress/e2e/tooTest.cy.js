describe("General Scripts", () => {
    beforeEach(() => {
        cy.visit("http://localhost:3000/");
        cy.get("#container > button:nth-child(2)").click();
        cy.wait(100);
    })
    it("getTodoFocus", () => {                
        cy.get("#title").type("maTodo");
        cy.get("#container > form:nth-child(2) > button:nth-child(5)").click();        
    })
    it("countTodo should be 1", () => {
        cy.get("#title").type("maTodo");
        cy.get("#container > form:nth-child(2) > button:nth-child(5)").click();   
        cy.get("#container > p:nth-child(4)").contains("1");
    })
})