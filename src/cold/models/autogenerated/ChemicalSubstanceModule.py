
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalEntityModule import ChemicalEntity



from .SubstanceModule import Substance







class ChemicalSubstance(ChemicalEntity, Substance):
    """
    Class representing the `ChemicalSubstance` entity, which inherits from:
    - ChemicalEntity, Substance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_df96cbb6_b5ee_4222_8eab_b3675df24bea'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChemicalSubstance'`
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
    obj = ChemicalSubstance(
    
    class_iri='https://w3id.org/emmo#EMMO_df96cbb6_b5ee_4222_8eab_b3675df24bea',
    
    class_name='ChemicalSubstance',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_df96cbb6_b5ee_4222_8eab_b3675df24bea',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChemicalSubstance',
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
    

    
    

    

    