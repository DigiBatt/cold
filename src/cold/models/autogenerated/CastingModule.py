
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromLiquidModule import FormingFromLiquid







class Casting(FormingFromLiquid):
    """
    Class representing the `Casting` entity, which inherits from:
    - FormingFromLiquid

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_ae3c9eb3_289d_4133_99d6_77068367a58d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Casting'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Casting(
    
    class_iri='https://w3id.org/emmo#EMMO_ae3c9eb3_289d_4133_99d6_77068367a58d',
    
    class_name='Casting',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_ae3c9eb3_289d_4133_99d6_77068367a58d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Casting',
        alias="class_name"
    )
    

    
    

    

    