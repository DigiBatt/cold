
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysioChemicalQuantityModule import PhysioChemicalQuantity



from .PureNumberQuantityModule import PureNumberQuantity







class StoichiometricNumberOfSubstance(PhysioChemicalQuantity, PureNumberQuantity):
    """
    Class representing the `StoichiometricNumberOfSubstance` entity, which inherits from:
    - PhysioChemicalQuantity, PureNumberQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_cbba91a7_d639_461f_ae23_d021751029e4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StoichiometricNumberOfSubstance'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StoichiometricNumberOfSubstance(
    
    class_iri='https://w3id.org/emmo#EMMO_cbba91a7_d639_461f_ae23_d021751029e4',
    
    class_name='StoichiometricNumberOfSubstance',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    wikidataReference="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_cbba91a7_d639_461f_ae23_d021751029e4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StoichiometricNumberOfSubstance',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    