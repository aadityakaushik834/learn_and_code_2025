// Does this Book class follow SRP?  

class Book {
 
    function getTitleOfBook() {
        return "A Great Book";
    }
 
    function getAuthorName() {
        return "John Doe";
    }
 
    function turnToNextPage() {
        // pointer to next page
    }
 
    function getCurrentPageContent() {
        return "current page content";
    }
 
    function getLocation() {
        // returns the position in the library
        // ie. shelf number & room number
    }

    function save() {
        $filename = '/documents/'. $this->getTitle(). ' - ' . $this->getAuthor();
        file_put_contents($filename, serialize($this));
    }
}

interface Printer {
    function printPage($page);
}
 
class PlainTextPrinter implements Printer {
    function printPage($page) {
        echo $page;
    }
 
}
 
class HtmlPrinter implements Printer {
    function printPage($page) {
        echo '<div style="single-page">' . $page . '</div>';
    }
}