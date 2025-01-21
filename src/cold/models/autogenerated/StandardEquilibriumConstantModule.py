
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EquilibriumConstantModule import EquilibriumConstant



from .PhysioChemicalQuantityModule import PhysioChemicalQuantity







class StandardEquilibriumConstant(EquilibriumConstant, PhysioChemicalQuantity):
    """
    Class representing the `StandardEquilibriumConstant` entity, which inherits from:
    - EquilibriumConstant, PhysioChemicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_672e2475_8376_4987_82cf_097f0024e74b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StandardEquilibriumConstant'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StandardEquilibriumConstant(
    
    class_iri='https://w3id.org/emmo#EMMO_672e2475_8376_4987_82cf_097f0024e74b',
    
    class_name='StandardEquilibriumConstant',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_672e2475_8376_4987_82cf_097f0024e74b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StandardEquilibriumConstant',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    