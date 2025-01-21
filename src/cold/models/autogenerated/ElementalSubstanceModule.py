
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalSubstanceModule import ChemicalSubstance







class ElementalSubstance(ChemicalSubstance):
    """
    Class representing the `ElementalSubstance` entity, which inherits from:
    - ChemicalSubstance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_436b11bd_1756_4821_9f14_c9ed6b67552e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElementalSubstance'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElementalSubstance(
    
    class_iri='https://w3id.org/emmo#EMMO_436b11bd_1756_4821_9f14_c9ed6b67552e',
    
    class_name='ElementalSubstance',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_436b11bd_1756_4821_9f14_c9ed6b67552e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElementalSubstance',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    