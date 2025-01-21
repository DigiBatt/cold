
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .GraphicalModule import Graphical







class Document(Graphical):
    """
    Class representing the `Document` entity, which inherits from:
    - Graphical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ccdc1a41_6e96_416b_92ec_efe67917434a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Document'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Document(
    
    class_iri='https://w3id.org/emmo#EMMO_ccdc1a41_6e96_416b_92ec_efe67917434a',
    
    class_name='Document',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ccdc1a41_6e96_416b_92ec_efe67917434a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Document',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    