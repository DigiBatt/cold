
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from ..custom.LinkedDataModelModule import LinkedDataModel








class Tebi(LinkedDataModel):
    """
    Class representing the `Tebi` entity, which inherits from:
    - LinkedDataModel

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#Tebi'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Tebi'`
        - **Alias**: `class_name`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Tebi(
    
    class_iri='https://w3id.org/emmo#Tebi',
    
    class_name='Tebi',
    
    hasSymbolValue="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#Tebi',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'Tebi',
        
        alias="class_name"
    )
    
    hasSymbolValue: Optional[str] = Field(
        
            None,
        
        alias="hasSymbolValue"
    )
    


    
    

    

    