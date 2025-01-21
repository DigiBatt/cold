
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PhysioChemicalQuantityModule import PhysioChemicalQuantity



from .ISQDimensionlessQuantityModule import ISQDimensionlessQuantity







class ThermalDiffusionRatio(PhysioChemicalQuantity, ISQDimensionlessQuantity):
    """
    Class representing the `ThermalDiffusionRatio` entity, which inherits from:
    - PhysioChemicalQuantity, ISQDimensionlessQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e84be61e_6f6f_43e2_b91d_86898a5dc7c4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ThermalDiffusionRatio'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ThermalDiffusionRatio(
    
    class_iri='https://w3id.org/emmo#EMMO_e84be61e_6f6f_43e2_b91d_86898a5dc7c4',
    
    class_name='ThermalDiffusionRatio',
    
    wikidataReference="example_value",
    
    qudtReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e84be61e_6f6f_43e2_b91d_86898a5dc7c4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ThermalDiffusionRatio',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    