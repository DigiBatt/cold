
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from ..custom.LinkedDataModelModule import LinkedDataModel








class Pebi(LinkedDataModel):
    """
    Class representing the `Pebi` entity, which inherits from:
    - LinkedDataModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#Pebi'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Pebi'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Pebi(
    
    class_iri='https://w3id.org/emmo#Pebi',
    
    class_name='Pebi',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#Pebi',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'Pebi',
        
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        
            None,
        
        alias="hasSymbolValue"
    )
    


    
    

    

    