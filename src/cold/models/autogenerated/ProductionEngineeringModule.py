
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ProcessEngineeringProcessModule import ProcessEngineeringProcess







class ProductionEngineering(ProcessEngineeringProcess):
    """
    Class representing the `ProductionEngineering` entity, which inherits from:
    - ProcessEngineeringProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_71b7346e_5a4a_4b2b_8ac5_d41ecc9c7bfd'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ProductionEngineering'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ProductionEngineering(
    
    class_iri='https://w3id.org/emmo#EMMO_71b7346e_5a4a_4b2b_8ac5_d41ecc9c7bfd',
    
    class_name='ProductionEngineering',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_71b7346e_5a4a_4b2b_8ac5_d41ecc9c7bfd',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ProductionEngineering',
        alias="class_name"
    )
    

    
    

    

    