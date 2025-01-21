
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .InorganicCompoundModule import InorganicCompound



from .WeakBaseCompoundModule import WeakBaseCompound







class IronIIIHydroxide(InorganicCompound, WeakBaseCompound):
    """
    Class representing the `IronIIIHydroxide` entity, which inherits from:
    - InorganicCompound, WeakBaseCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_323a2e39_d7d5_4802_884a_9aa41a280986'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IronIIIHydroxide'`
        - **Alias**: `class_name`
    
    - `IUPACName` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IUPACName`
    
    - `pubChemReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `pubChemReference`
    
    - `standardInChI` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `standardInChI`
    
    - `molecularFormula` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `molecularFormula`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IronIIIHydroxide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_323a2e39_d7d5_4802_884a_9aa41a280986',
    
    class_name='IronIIIHydroxide',
    
    IUPACName="example_value",
    
    pubChemReference="example_value",
    
    standardInChI="example_value",
    
    molecularFormula="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_323a2e39_d7d5_4802_884a_9aa41a280986',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IronIIIHydroxide',
        alias="class_name"
    )
    
    IUPACName: Optional[str] = Field(
        None,
        alias="IUPACName"
    )
    
    pubChemReference: Optional[str] = Field(
        None,
        alias="pubChemReference"
    )
    
    standardInChI: Optional[str] = Field(
        None,
        alias="standardInChI"
    )
    
    molecularFormula: Optional[str] = Field(
        None,
        alias="molecularFormula"
    )
    

    
    

    

    