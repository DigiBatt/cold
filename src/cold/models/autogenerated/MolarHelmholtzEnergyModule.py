
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysioChemicalQuantityModule import PhysioChemicalQuantity



from .MolarEnergyModule import MolarEnergy







class MolarHelmholtzEnergy(PhysioChemicalQuantity, MolarEnergy):
    """
    Class representing the `MolarHelmholtzEnergy` entity, which inherits from:
    - PhysioChemicalQuantity, MolarEnergy

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_aea43ae4_f824_4c42_892e_709bf9dc1c40'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MolarHelmholtzEnergy'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MolarHelmholtzEnergy(
    
    class_iri='https://w3id.org/emmo#EMMO_aea43ae4_f824_4c42_892e_709bf9dc1c40',
    
    class_name='MolarHelmholtzEnergy',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_aea43ae4_f824_4c42_892e_709bf9dc1c40',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MolarHelmholtzEnergy',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    